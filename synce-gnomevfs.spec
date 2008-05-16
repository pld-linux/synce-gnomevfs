Summary:	GnomeVFS module for accessing Windows CE and Pocket PC devices
Summary(pl.UTF-8):	Moduł GnomeVFS służący do dostępu do urządzeń Windows CE i Pocket PC
Name:		synce-gnomevfs
Version:	0.11.1
Release:	1
License:	MIT
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/synce/%{name}-%{version}.tar.gz
# Source0-md5:	3f4d3134e9187ffe518353b59a2f9b40
URL:		http://www.synce.org/
BuildRequires:	automake
BuildRequires:	gnome-vfs2-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	synce-librapi2-devel >= %{version}
%requires_eq_to	synce-librapi2 synce-librapi2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SynCE-GnomeVFS is a GnomeVFS module for accessing Windows CE and
Pocket PC devices. It is part of the SynCE project:
<http://www.synce.org/>.

%description -l pl.UTF-8
SynCE-GnomeVFS to moduł GnomeVFS służący do dostępu do urządzeń
Windows CE i Pocket PC. Jest on częścią projektu SynCE:
<http://www.synce.org/>.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* .
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/gnome-vfs-2.0/modules/*.la
rm $RPM_BUILD_ROOT%{_libdir}/synce-trayicon/modules/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README
%attr(755,root,root) %{_bindir}/synce-in-computer-folder
%attr(755,root,root) %{_libdir}/gnome-vfs-2.0/modules/libsyncevfs.so
%attr(755,root,root) %{_libdir}/synce-trayicon/modules/gnomevfs-trayicon-module.so
%{_sysconfdir}/gnome-vfs-2.0/modules/synce-module.conf
%{_iconsdir}/hicolor/*/apps/synce-gnomevfs.png
# dir shared with synce-rra, synce-software-manager, synce-trayicon
%dir %{_datadir}/synce
%attr(755,root,root) %{_datadir}/synce/synce-in-computer-folder.sh
%{_mandir}/man1/synce-in-computer-folder.1*
