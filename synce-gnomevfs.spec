Summary:	GnomeVFS module for accessing Windows CE and Pocket PC devices
Summary(pl):	Modu³ GnomeVFS s³u¿±cy do dostêpu do urz±dzeñ Windows CE i Pocket PC
Name:		synce-gnomevfs
Version:	0.9.0
Release:	0.2
License:	MIT
Vendor:		The SynCE Project
Group:		Applications/Communications
Source0: 	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	1fa8d653297331479edcd5d983a0f75e
URL:		http://synce.sourceforge.net/
BuildRequires:	synce-devel = %{version}
Requires:	synce
# XXX: gnomevfs deps missing
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GnomeVFS is a GnomeVFS module for accessing Windows CE and
Pocket PC devices. It is part of the SynCE project:
http://synce.sourceforge.net/ .

%description -l pl
SynCE-GnomeVFS to modu³ GnomeVFS s³u¿±cy do dostêpu do urz±dzeñ
Windows CE i Pocket PC. Jest on czê¶ci± projektu SynCE:
http://synce.sourceforge.net/ .

%prep
%setup -q 

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/synce-in-computer-folder
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libsyncevfs.so
%{_sysconfdir}/gnome-vfs-2.0/modules/synce-module.conf
%{_pixmapsdir}/synce/synce-color.png
%{_datadir}/synce/synce-in-computer-folder.sh
